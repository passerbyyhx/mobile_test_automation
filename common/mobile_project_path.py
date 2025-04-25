import pathlib
from os.path import join


class MobileProjectPath:
    def __init__(self):
        self.root_path: str = str(pathlib.Path(__file__).parent.parent.absolute())
        self.allure_results_path: str = join(self.root_path, "allure-results")
        self.common_path: str = join(self.root_path, "common")
        self.features_path: str = join(self.root_path, "features")
        self.mobile_elements_path: str = join(self.root_path, "mobile_elements")
        self.screenshots_path: str = join(self.root_path, "screenshots")
        self.steps_path: str = join(self.root_path, "steps")


    @staticmethod
    def get_path(*args):
        path = ""
        for i in range(len(args)):
            if i == 0:
                path = args[i]
            else:
                path = join(path, args[i])
        return path
