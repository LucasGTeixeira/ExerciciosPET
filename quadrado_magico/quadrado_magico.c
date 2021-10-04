#include <stdio.h>
#include<stdlib.h>

int analisa_quadrado();
	
int main(){
	analisa_quadrado();
}

int analisa_quadrado(){
	//variáveis a serem usadas na função
	int N, i, j;
	
	
	//capturando o tamanho da matriz quadrada NxN
	do{
		scanf("%d", &N);
	}while(N>2 && N<10);
	
	//criando Matriz e suas linhas
	int linha[N];
	int Matriz[N][N]
	
	//capturando dados de cada linha
	//para cada linha
	for (i=0;i<N;i++){
		//para cada coluna
		for (j=0;i<N;j++){
			scanf("%d", &Matriz[i][j]);
		}
	}
	
	//print para teste
	//para cada linha
	for (i=0;i<N;i++){
		//para cada coluna
		for (j=0;i<N;j++){
			printf("%d", Matriz[i][j]);
		}
	}
}
