from dotenv import load_dotenv
import os

#  ____________________________________________________________
# │ REQUIRED CONFIGURATION SECTION                             │
# │ ------------------------------                             │
# │ This is the ONLY part of this file you should modify.      │
# │ Add your required environment variables below.             │
# │ Each key is the variable name, and the value is its type.  │
# |____________________________________________________________|

REQUIRED_VARS: dict[str, type[object]] = {"N_ITER": int}

#  ____________________________________________________________
# │ DO NOT MODIFY ANYTHING BELOW THIS LINE                     │
# | --------------------------------------                     |
# │ The rest of this file handles loading and validation.      │
# │ Changing it may break config loading across the project.   │
# |____________________________________________________________|


class EnvConfig:
    def __init__(self, required_vars):
        self._config = {}
        self._validate_env()
        load_dotenv()
        self._load_env_vars(required_vars)

    def _validate_env(self):
        if not os.path.exists(".env"):
            raise FileNotFoundError(".env file not found. Please create one")

    def _load_env_vars(self, required_vars):
        # create an empty list that will contain the missing environment variables (if any)
        missing = []

        # try to load all environment variables, assign them to config variables
        # and see if any are missing or cannot be cast to their appropriate type
        for var, cast in required_vars.items():
            value = os.getenv(var)
            if value is None:
                missing.append(var)
            else:
                try:
                    self._config[var] = cast(value)
                except ValueError:
                    raise ValueError(
                        f"Environment variable {var} could not be cast to {cast.__name__}"
                    )

        # if any environment variable is missing, raise an error
        if missing:
            missing_vars = ", ".join(missing)
            raise EnvironmentError(
                f"Missing required environment variables: {missing_vars}\n"
                "Please ensure your .env file includes all necessary keys."
            )

    def __getattr__(self, name):
        if name in self._config:
            return self._config[name]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )


config = EnvConfig(REQUIRED_VARS)
