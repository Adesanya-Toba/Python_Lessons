from abc import ABC, abstractmethod
from pathlib import Path
import zipfile
import fnmatch
import re
from PIL import Image


class ZipProcessor(ABC):
    """
    As this is subclass of an ABC, it allows us to provide placeholders
    instead of methods.
    """

    def __init__(self, archive: Path) -> None:
        self.archive_path = archive
        self._pattern: str

    def process_files(self, pattern: str) -> None:
        self._pattern = pattern
        input_path, output_path = self.make_backup()

        with zipfile.ZipFile(output_path, "w") as output:
            with zipfile.ZipFile(input_path) as input:
                self.copy_and_transform(input, output)

    def make_backup(self) -> tuple[Path, Path]:
        input_path = self.archive_path.with_suffix(f"{self.archive_path.suffix}.old")
        output_path = self.archive_path
        self.archive_path.rename(input_path)
        return input_path, output_path

    def copy_and_transform(
        self, input: zipfile.ZipFile, output: zipfile.ZipFile
    ) -> None:
        for item in input.infolist():
            extracted = Path(input.extract(item))
            if self.matches(item):
                print(f"Transform {item}")
                self.transform(extracted)
            else:
                print(f"Ignore      {item}")
            output.write(extracted, item.filename)
            self.remove_under_cwd(extracted)

    def matches(self, item: zipfile.ZipInfo) -> bool:
        """Method to match filenames within the zip file."""
        return not item.is_dir() and fnmatch.fnmatch(item.filename, self._pattern)

    def remove_under_cwd(self, extracted: Path) -> None:
        """Clean-up temporary files and directories created by the extraction
        process."""
        extracted.unlink()
        for parent in extracted.parents:
            if parent == Path.cwd():
                break
            parent.rmdir()

    @abstractmethod
    def transform(self, extracted: Path) -> None:
        """Abstract method that is defined in the subclasses that inherit
        this class."""
        ...


class TextTweaker(ZipProcessor):
    """Class to find and replace text in pattern matched files.
    Replica of what we have in the Manager_objects.py but this re-uses a
    ZipProcessor class which unzips"""

    def __init__(self, archive: Path) -> None:
        super().__init__(archive)  # Initialize the parent class
        self.find: str
        self.replace: str

    def find_and_replace(self, find: str, replace: str) -> "TextTweaker":
        self.find = find
        self.replace = replace
        return self

    def transform(self, extracted: Path) -> None:
        input_text = extracted.read_text()
        output_text = re.sub(self.find, self.replace, input_text)
        extracted.write_text(output_text)


class ImgTweaker(ZipProcessor):
    """Class to scale images within a zipfile.
    Easier to write since we already have a ZipProcessor class.
    """

    def transform(self, extracted: Path) -> None:
        image = Image.open(extracted)
        scaled = image.resize(size=(640, 960))
        scaled.save(extracted)


def main():
    TextTweaker(Path("Py3_OOP/Chpt5_UsingOOP/sample.zip")).find_and_replace(
        "xyzzy", "plover'egg"
    ).process_files("*.md")

    ImgTweaker(Path("Py3_OOP/Chpt5_UsingOOP/sample_img.zip")).process_files("*.jpg")


if __name__ == "__main__":
    main()
