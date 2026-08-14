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