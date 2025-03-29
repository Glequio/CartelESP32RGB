#include <FastLED.h>
//#include <map>
//#include <vector>
//#include <iostream>

// Configuración de los LEDs

#define DATA_PIN 2

const uint8_t NMATRIZ = 3;
const uint8_t COL = 8;
const uint8_t ROW = 8;
const uint8_t SP = 1;

const int NUM_LEDS = NMATRIZ * COL * ROW;
const bool ZIGZAG = false;
uint8_t red = 6;
uint8_t green = 6;
uint8_t blue = 0;


//Caracteres

String texto = "AAAÑÑÑÑÑÑL";

const uint8_t A[] = { 0b00111110, 0b01111110, 0b11011000, 0b10011000, 0b11011000, 0b01111110, 0b00111110 };
const uint8_t B[] = { 0b11111110, 0b11111110, 0b10010010, 0b10010010, 0b11111110, 0b01101100 };
const uint8_t C[] = { 0b01111100, 0b11111110, 0b10000010, 0b10000010, 0b11000110, 0b01000100 };
const uint8_t D[] = { 0b11111110, 0b11111110, 0b10000010, 0b10000010, 0b01111100, 0b00111000 };
const uint8_t E[] = { 0b11111110, 0b11111110, 0b11010110, 0b11000110, 0b11000110 };
const uint8_t F[] = { 0b11111110, 0b11111110, 0b11010000, 0b11010000, 0b11000000 };
const uint8_t G[] = { 0b01111100, 0b11111110, 0b10000010, 0b10011010, 0b11011010, 0b01011100 };
const uint8_t H[] = { 0b11111110, 0b11111110, 0b00010000, 0b00010000, 0b11111110, 0b11111110 };
const uint8_t I[] = { 0b11000110, 0b11111110, 0b11111110, 0b11000110 };
const uint8_t J[] = { 0b00000110, 0b11000110, 0b11111100, 0b11111000, 0b11000000 };
const uint8_t K[] = { 0b11111110, 0b11111110, 0b00110000, 0b01111100, 0b11001110, 0b11000110 };
const uint8_t L[] = { 0b11111110, 0b11111110, 0b00000110, 0b00000110, 0b00000110 };
const uint8_t M[] = { 0b11111110, 0b11111110, 0b01100000, 0b00110000, 0b01100000, 0b11111110, 0b11111110 };
const uint8_t N[] = { 0b11111110, 0b11111110, 0b01100000, 0b00110000, 0b00011000, 0b11111110, 0b11111110 };
const uint8_t n[] = { 0b00111110, 0b10111110, 0b10011000, 0b10001100, 0b10111110, 0b00111110 };
const uint8_t O[] = { 0b01111100, 0b11111110, 0b11111110, 0b11111110, 0b11111110, 0b11111110, 0b01111100 };
const uint8_t P[] = { 0b11111110, 0b11111110, 0b10001000, 0b10001000, 0b11111000, 0b01110000 };
const uint8_t Q[] = {};
const uint8_t R[] = {};
const uint8_t S[] = {};
const uint8_t T[] = {};
const uint8_t U[] = {};
const uint8_t V[] = {};
const uint8_t W[] = {};
const uint8_t X[] = {};
const uint8_t Y[] = {};
const uint8_t Z[] = {};
const uint8_t DE[] = { 0b11000011, 0b01100110, 0b00111100, 0b00011000 };  // Caracter >
const uint8_t IZ[] = { 0b00011000, 0b00111100, 0b01100110, 0b11000011 };  // Caracter >


CRGB leds[NUM_LEDS];

int barrido(int x, int y) {
  if (x < 0 && x >= COL * NMATRIZ && y < 0 && y >= ROW) {
    return -1;  // Devuelvo -1 si esta fuera de limite
  } else {
    byte nmat = x / COL + 1;  // Determinar en qué matriz está el LED
    x = x % COL;              // Ajustar x para que sea relativo a la matriz
    if (ZIGZAG) {
      if (y % 2 == 1) {
        return (COL * (y + 1) - 1 - x) + ((nmat - 1) * COL * ROW);
      } else {
        return (COL * y + x) + ((nmat - 1) * COL * ROW);
      }
    } else {
      return (y * COL + x) + ((nmat - 1) * COL * ROW);
    }
  }
}
//  Tamaño char
int columnChar(char character) {
  uint8_t charLength = 0;

  switch (character) {
    case 'A':
      charLength = sizeof(A) / sizeof(A[0]);
      break;
    case 'B':
      charLength = sizeof(B) / sizeof(B[0]);
      break;
    case 'C':
      charLength = sizeof(C) / sizeof(C[0]);
      break;
    case 'D':
      charLength = sizeof(D) / sizeof(D[0]);
      break;
    case 'E':
      charLength = sizeof(E) / sizeof(E[0]);
      break;
    case 'F':
      charLength = sizeof(F) / sizeof(F[0]);
      break;
    case 'G':
      charLength = sizeof(G) / sizeof(G[0]);
      break;
    case 'H':
      charLength = sizeof(H) / sizeof(H[0]);
      break;
    case 'I':
      charLength = sizeof(I) / sizeof(I[0]);
      break;
    case 'J':
      charLength = sizeof(J) / sizeof(J[0]);
      break;
    case 'K':
      charLength = sizeof(K) / sizeof(K[0]);
      break;
    case 'L':
      charLength = sizeof(L) / sizeof(L[0]);
      break;
    case 'M':
      charLength = sizeof(M) / sizeof(M[0]);
      break;
    case 'N':
      charLength = sizeof(N) / sizeof(N[0]);
      break;
    case 'n':
      Serial.println("enie encontrada");
      charLength = sizeof(n) / sizeof(n[0]);
      break;      
    case 'O':
      charLength = sizeof(O) / sizeof(O[0]);
      break;
    case 'P':
      charLength = sizeof(P) / sizeof(P[0]);
      break;
    case 'Q':
      charLength = sizeof(Q) / sizeof(Q[0]);
      break;
    case 'R':
      charLength = sizeof(R) / sizeof(R[0]);
      break;
    case 'S':
      charLength = sizeof(S) / sizeof(S[0]);
      break;
    case 'T':
      charLength = sizeof(T) / sizeof(T[0]);
      break;
    case 'U':
      charLength = sizeof(U) / sizeof(U[0]);
      break;
    case 'V':
      charLength = sizeof(V) / sizeof(V[0]);
      break;
    case 'W':
      charLength = sizeof(W) / sizeof(W[0]);
      break;
    case 'X':
      charLength = sizeof(X) / sizeof(X[0]);
      break;
    case 'Y':
      charLength = sizeof(Y) / sizeof(Y[0]);
      break;
    case 'Z':
      charLength = sizeof(Z) / sizeof(Z[0]);
      break;

    case '>':
      charLength = sizeof(DE) / sizeof(DE[0]);
      break;
    case '<':
      charLength = sizeof(IZ) / sizeof(IZ[0]);
      break;
    // Añadir más casos para otros caracteres aquí
    default:
      return 0;  // No hacemos nada si el carácter no está definido
  }
  return charLength;
}

// Tamaño Texto

int zText(String texto) {
  int Ztexto = 0;
  for (int k = 0; k < texto.length(); k++) {
    Ztexto = Ztexto + columnChar(texto[k]) + SP;
  }
  return Ztexto;
}


// Función para mostrar un carácter en una posición específica
void muestraChar(char caracter, int x, int y) {
  const uint8_t *charData = nullptr;
  uint8_t charLength = 0;
  Serial.println(caracter);

  switch (caracter) {
    case 'A':
      charData = A;
      charLength = columnChar('A');
      break;
    case 'B':
      charData = B;
      charLength = columnChar('B');
      break;
    case 'C':
      charData = C;
      charLength = columnChar('C');
      break;
    case 'D':
      charData = D;
      charLength = columnChar('D');
      break;
    case 'E':
      charData = E;
      charLength = columnChar('E');
      break;
    case 'F':
      charData = F;
      charLength = columnChar('F');
      break;
    case 'G':
      charData = G;
      charLength = columnChar('G');
      break;
    case 'H':
      charData = H;
      charLength = columnChar('H');
      break;
    case 'I':
      charData = I;
      charLength = columnChar('I');
      break;
    case 'J':
      charData = J;
      charLength = columnChar('J');
      break;
    case 'K':
      charData = K;
      charLength = columnChar('K');
      break;
    case 'L':
      charData = L;
      charLength = columnChar('L');
      break;
    case 'M':
      charData = M;
      charLength = columnChar('M');
      break;
    case 'N':
      charData = N;
      charLength = columnChar('N');
      break;
    case 'n':
      Serial.println("Ñ enconrada");
      charData = n;
      charLength = sizeof(n) / sizeof(n[0]);//columnChar('ENIE');
      break;      
    case 'O':
      charData = O;
      charLength = columnChar('O');
      break;
    case 'P':
      charData = P;
      charLength = columnChar('P');
      break;
    case 'Q':
      charData = Q;
      charLength = columnChar('Q');
      break;
    case 'R':
      charData = R;
      charLength = columnChar('R');
      break;
    case 'S':
      charData = S;
      charLength = columnChar('S');
      break;
    case 'T':
      charData = T;
      charLength = columnChar('T');
      break;
    case 'U':
      charData = U;
      charLength = columnChar('U');
      break;
    case 'V':
      charData = V;
      charLength = columnChar('V');
      break;
    case 'W':
      charData = W;
      charLength = columnChar('W');
      break;
    case 'X':
      charData = X;
      charLength = columnChar('X');
      break;
    case 'Y':
      charData = Y;
      charLength = columnChar('Y');
      break;
    case 'Z':
      charData = Z;
      charLength = columnChar('Z');
      break;

    case '>':
      charData = DE;  // Asumiendo que '>' es lo que representa DE en tu código
      charLength = sizeof(DE) / sizeof(DE[0]);   //columnChar('DE');
      break;
    case '<':
      charData = IZ;
      charLength = sizeof(IZ) / sizeof(IZ[0]);
      break;
    // Añadir más casos para otros caracteres aquí
    default:
      return;  // No hacemos nada si el carácter no está definido
  }
  uint8_t i;
  if (-x < charLength && x < 0 && x < (COL * NMATRIZ)) {
    i = -x;
  } else {
    i = 0;
  }
  for (; i < charLength; i++) {
    for (uint8_t j = 0; j < COL; j++) {
      if (charData[i] & (1 << (7 - j))) {
        if ((y + j) < ROW && (y + j) >= 0 && x < COL * NMATRIZ && (x + i) >= 0) {
          leds[barrido(x + i, y + j)] = CRGB(0, 1, 2);
        }
      }
    }
  }
}

/*
·························································································································
Funcion Scroll: produce la animacion de scoll del texto ingresado, pudiendo correr a la derecha o a la izquierda, 
El punto de arranque es el xo yo, siendo este el punto superior izquierdo del caracter. speed es la velocidad de la animacion
siendo 120 el valor mas lento y 20 el mas rapido.
La direccion se controla con direction true <----, false ---->
·························································································································
*/
void textPrint(int xo, int yo, String texto) {
  FastLED.clear();
  int puntero = xo;
  int Ztexto = 0;
  uint8_t charLength;
  Ztexto = zText(texto);
  if (xo < COL * NMATRIZ && yo > -7 && xo > -Ztexto && yo < ROW) {
    for (int i = 0; i < texto.length() && puntero < COL * NMATRIZ + 1;) {
      //Serial.println(texto[i]);
      if (texto[i] == (char)0xC3 && i + 1 < texto.length() && texto[i + 1] == (char)0x91) {
      //  Serial.println("Ñ");
        muestraChar('n', puntero, 1);
        puntero = columnChar('Ñ') + puntero + SP;
        i += 2; // Saltar los 2 bytes de Ñ
      } else {
      //Serial.println(texto[i]);
      muestraChar(texto[i], puntero, 1);
      puntero = columnChar(texto[i]) + puntero + SP;
      i++;
      }

    }
  }
  FastLED.show();
}

void setup() {
  // Inicializar la tira de LEDs
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  Serial.begin(115200);
}

void loop() {
//  Serial.println(texto);
//  for (int i = 0; i < texto.length();) {
//    if (texto[i] == (char)0xC3 && i + 1 < texto.length() && texto[i + 1] == (char)0x91) {
//      Serial.println("Ñ");
//      i += 2; // Saltar los 2 bytes de Ñ
//    } else {
//      Serial.println(texto[i]);
//      i++;
//    }
//    delay(2000);
 // }

  for (int i = COL * NMATRIZ + 5; i > -zText(texto); i--) {
    textPrint(i, 1, texto);
    //    Serial.println(i);
    //    Serial.println(texto.length());
    delay(130);
  }
}
