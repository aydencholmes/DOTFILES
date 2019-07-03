from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Basic theme which only uses colors in 0-15 range"""
    USERNAME_FG = 1
    USERNAME_BG = 1
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 1
    HOSTNAME_BG = 1

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = 13
    HOME_FG = 7
    PATH_BG = 4 
    PATH_FG = 8 # light grey
    CWD_BG = 0
    CWD_FG = 7
    SEPARATOR_FG = 67 

    READONLY_BG = 1
    READONLY_FG = 15

    REPO_CLEAN_BG = 2   # green
    REPO_CLEAN_FG = 0   # black
    REPO_DIRTY_BG = 1   # red
    REPO_DIRTY_FG = 15  # white

    JOBS_FG = 14
    JOBS_BG = 1

    CMD_PASSED_BG = 3
    CMD_PASSED_FG = 13
    CMD_FAILED_BG = 3
    CMD_FAILED_FG = 13

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 110
    VIRTUAL_ENV_FG = 234 

    AWS_PROFILE_FG = 234
    AWS_PROFILE_BG = 110

    TIME_FG = 8
    TIME_BG = 7
