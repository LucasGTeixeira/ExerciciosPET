#include <stdio.h>
#include <stdlib.h>

int main(){
	int i, j, linhas, colunas, cont = 1;
	int fimDaToca=0;
	
	int x, y;
	int posicaoInicial[2];
	
	scanf("%d %d", &linhas, &colunas);
	
	int Toca[linhas][colunas];
	for (i=0; i<linhas; i++){
		for (j=0; j<colunas; j++){
			scanf("%d", &Toca[i][j]);
			if(Toca[i][j] == 3){
				posicaoInicial[0] = i;
				posicaoInicial[1] = j;
			}
		}
	}
	
	x = posicaoInicial[0]; //posi��o da liinha inicial
	y = posicaoInicial[1]; //posi��o da coluna inicial
	
	//percorrendo a toca at� encontrar o fim dela
	while (!fimDaToca){
		//analisa o item de mesma coluna na linha de cima (caso exista)
		if(x-1 >= 0 && Toca[x-1][y] == 1){
			Toca[x][y] = -1;
			//nova posi��o ser� Toca[x-1][y]
			x--;
			cont++;
		}
		//analisa linha de baixo (caso n�o estoure a matriz)
		else if(x+1 < linhas && Toca[x+1][y] == 1){
			Toca[x][y] = -1;
			//nova posi��o ser� Toca[x+1][y]
			x++;
			cont++;
		}
		//coluna da direita (caso n�o estoure a matriz)
		else if(y+1 < colunas&& Toca[x][y+1] == 1){
			Toca[x][y] = -1;
			//nova posi��o ser� Toca[x][y+1]
			y++;
			cont++;
		}
		//coluna da esquerda (caso exista)
		else if(y-1 >= 0 && Toca[x][y-1] == 1){
			Toca[x][y] = -1;
			//nova posi��o ser� Toca[x][y-1]
			y--;
			cont++;
		}
		else{
			if((x-1 >= 0 && Toca[x-1][y] == 2) || 
			(x+1 >= 0 && Toca[x+1][y] == 2) ||
			(y+1 < colunas&& Toca[x][y+1] == 2) ||
			(y-1 < colunas&& Toca[x][y-1] == 2)){
				//caso o n�mero 2 seja encontrado em qualquer um dos lados da posi��o atual
				cont++;
				fimDaToca = 1;
			}
			//caso contrario, o caminho percorrido � interrompido e voltamos para o inicio da toca
			else{
				Toca[x][y] = -1;
				x = posicaoInicial[0];
				y = posicaoInicial[1];
				cont = 1;
			}
		}	
	}
	printf("%d", cont);
}
