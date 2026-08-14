       IDENTIFICATION DIVISION.
       PROGRAM-ID. SOMA-NUMEROS.
       AUTHOR. LUIZ

       ENVIRONMENT DIVISION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-NUM1        PIC 9(05) VALUE ZEROS.
       01  WS-NUM2        PIC 9(05) VALUE ZEROS.
       01  WS-RESULTADO   PIC 9(06) VALUE ZEROS.

       *> Variável formatada para exibir o resultado sem zeros à esquerda
       01  WS-RESULT-EDIT PIC ZZZ,ZZ9.

       PROCEDURE DIVISION.
       0000-MAIN.
           DISPLAY "----------------------------------"
           DISPLAY "    SOMA DE DOIS NUMEROS EM COBOL "
           DISPLAY "----------------------------------"
           
           DISPLAY "Digite o primeiro numero: "
           ACCEPT WS-NUM1
           
           DISPLAY "Digite o segundo numero: "
           ACCEPT WS-NUM2
           
           *> Realiza a soma dos dois valores
           ADD WS-NUM1 WS-NUM2 TO WS-RESULTADO
           
           *> Move para a variável de edição para formatar a saída
           MOVE WS-RESULTADO TO WS-RESULT-EDIT
           
           DISPLAY "----------------------------------"
           DISPLAY "RESULTADO: " WS-RESULT-EDIT
           DISPLAY "----------------------------------"
           
           STOP RUN.