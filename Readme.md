Um projeto que **desliga o computador** quando você mostra o **dedo do meio** para a webcam.

Este projeto usa **MediaPipe** e **OpenCV** para detectar gestos da mão em tempo real e, se for detectado o gesto do dedo médio levantado com os demais abaixados, ele inicia o desligamento da máquina após 1 segundos de confirmação.



1. Clone o repositório:

    git clone https://github.com/PedroPiana/shutdown_gesture.git
    cd shutdown_gesture

2. Crie um ambiente virtual:

    python -m venv venv
    venv\Scripts\activate  # No Windows
    source venv/bin/activate  # No Linux/macOS


3. Instale as dependências:

    pip install -r requirements.txt

4. Rode o programa:

    python shutdown.py
