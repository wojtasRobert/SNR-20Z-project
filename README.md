# SNR-20Z-project
Projekt z przedmiotu Sieci Neuronowe.

- [SNR-20Z-project](#snr-20z-project)
- [Zadania do wykonania](#zadania-do-wykonania)
- [Rozwiązanie powinno zawierać:](#rozwiązanie-powinno-zawierać)
- [Run the project:](#run-the-project)
  - [1. Create virtual env](#1-create-virtual-env)
    - [On macOS and Linux:](#on-macos-and-linux)
    - [On Windows:](#on-windows)
  - [2. Activating a virtual environment](#2-activating-a-virtual-environment)
    - [On macOS and Linux:](#on-macos-and-linux-1)
    - [On Windows:](#on-windows-1)
  - [3. Requirements Files](#3-requirements-files)
    - [Unix/macOS](#unixmacos)
    - [Windows](#windows)
    - [Remember!](#remember)
  - [4. Download data](#4-download-data)
- [Przydatne linki](#przydatne-linki)

# Zadania do wykonania

1. Uczenie klasyfikatora
   * Zastosować wstępnie wytrenowaną sieć do ​uczenia tylko części klasyfikującej (ostatnie warstwy o połączeniach kompletnych)
   * Zanalizować wyniki klasyfikacji.
   * Zastąpić część klasyfikującą sieci przez ​SVM dla jądra liniowego, kwadratowego i wykładniczego.
   * Zanalizować wyniki klasyfikacji. W szczególności, zbadać efekt dopuszczenia błędnych klasyfikacji, porównać z wynikami 1a.
2. Uczenie sieci głębokiej
   * Przeprowadzić uczenie ​ostatniej warstwy splotowej​ wraz z częścią klasyfikującą.
   * Przeprowadzić uczenie ​dwóch ostatnich warstw splotowych wraz z częścią klasyfikującą.
   * Wytrenować ​całą sieć​ dla zadanych danych.
   * Uprościć strukturę sieci wytrenowanej w zadaniu 2c (np. poprzez usunięcie jednej lub więcej końcowych warstw splotowych, usunięcie warstw regularyzujących itp.) i ponowić uczenie.
   * Zanalizować wyniki.
3. Wizualizacja
   * Dokonać ​wizualizacji obszarów uwagi sieci wytrenowanych w zadaniu 1 oraz 2 z wykorzystaniem metod Class Activation Map (CAM)
   * Dokonać​ wizualizacji aktywacji wewnętrznych warstw sieci z wykorzystaniem techniki DeepDream. W każdym przypadku należy podzielić dane na uczące, walidacyjne i testujące. 
4. ​Zwielokrotnić zbiór danych z wykorzystaniem technik **data augmentation**. 
    
# Rozwiązanie powinno zawierać:

1. Analizę działania każdej z wersji zadania, porównanie wyników uzyskanych dla różnych wariantów, wizualizację obszarów uwagi wybranych struktur oraz wnioski z tych działań wypływające.
2. Ocenę – z punktu widzenia zaawansowanego użytkownika – narzędzi programistycznych zastosowanych przy rozwiązywaniu problemów.
   
# Run the project:

## 1. Create virtual env
### On macOS and Linux:

`python3 -m venv env`

### On Windows:

`py -m venv env`

## 2. Activating a virtual environment
### On macOS and Linux:

`source env/bin/activate`

### On Windows:

`.\env\Scripts\activate`

## 3. Requirements Files
### Unix/macOS 

`python -m pip install -r requirements.txt`

### Windows

`py -m pip install -r requirements.txt`

### Remember!

If you install new packages, update requirements.txt using:

`pip freeze > requirements.txt`

## 4. Download data
`./download_data.sh`


# Przydatne linki
https://towardsdatascience.com/step-by-step-vgg16-implementation-in-keras-for-beginners-a833c686ae6c

https://jacobgil.github.io/deeplearning/class-activation-maps

https://www.pyimagesearch.com/2020/03/09/grad-cam-visualize-class-activation-maps-with-keras-tensorflow-and-deep-learning/

https://hackernoon.com/deep-dream-with-tensorflow-a-practical-guide-to-build-your-first-deep-dream-experience-f91df601f479

https://www.tensorflow.org/tutorials/images/data_augmentation

https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks/

