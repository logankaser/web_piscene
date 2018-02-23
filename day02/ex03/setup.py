from distutils.core import setup, Extension

users = Extension("users", sources=["users.c"])

setup(name="Users",
    version = "1.0",
    description = "Get logged users",
    ext_modules = [users]
    )
