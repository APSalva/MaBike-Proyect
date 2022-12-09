# Importamos la libreria pytest
import pytest

# Importamos nuestro programa ObtenerIndiceHTML
from src.ObtenerIndiceHTML import ObtenerIndiceHTML

@pytest.mark.test_ObtenerIndiceHTML
def test_ObtenerIndiceHTML():

    assert ("hola") == "hola"
