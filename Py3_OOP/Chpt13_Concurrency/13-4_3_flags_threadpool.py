from concurrent import futures
import importlib
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(processName)-11s %(threadName)-11s [%(levelname)s]: %(message)s",
)
logger = logging.getLogger()

flags = importlib.import_module("13-4_2_flags")
# import flags.save_flag
print(flags)


def download_one(cc: str):
    image = flags.get_flag(cc)
    flags.save_flag(image, f"{cc}.gif")
    # print(cc, end=' ', flush=True)
    return cc


# def download_many(cc_list:list[str]) -> int:
#     with futures.ThreadPoolExecutor() as executor:
#         res = executor.map(download_one, sorted(cc_list))
#         # print(executor._threads)
#     return len(list(res))


# Using futures.ThreadPoolExecutor
def download_many_as_completed(cc_list: list[str]) -> int:
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            logger.info(f"Scheduled for {cc}: {future}")

        print()
        # time.sleep(4)

        # as_completed yields futures as they are completed.
        for count, future in enumerate(futures.as_completed(to_do), 1):
            res: str = future.result()
            logger.info(f"{future} result: {res!r}")

    return count  # type:ignore


# Using futures.ProcessPoolExecutor
def download_many_as_completed_process_pool(cc_list: list[str]) -> int:
    cc_list = cc_list[:5]
    with futures.ProcessPoolExecutor(max_workers=8) as executor:
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            logger.info(f"Scheduled for {cc}: {future}")

        print()
        # time.sleep(4)

        for count, future in enumerate(futures.as_completed(to_do), 1):
            res: str = future.result()
            logger.info(f"{future} result: {res!r}")

    return count  # type:ignore


if __name__ == "__main__":
    flags.main(download_many_as_completed)
