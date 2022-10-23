from main import multiply
#
# class

import pytest
import pytest.asyncio

class TestSymple:

    @pytest.mark.asyncio
    async def test_multiply(self):
            assert await multiply(2, 4) == 8


# pytest-cov - анализ процента покрытия тестами
# pylint
# flake8

# e308 - оттупы

# CI/CD continiosly intergration continues delivery

django-admin startproject
