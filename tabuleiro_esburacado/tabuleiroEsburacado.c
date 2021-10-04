#include <stdio.h>
#include <stdlib.h>

int calculaMovimento(){
	int numMovimentos = 0;
	
	/* modificar valores
	   conferir se valor modificado agora ocupa a casa 0
	   conferir se o valor modificado está dentro do conjunto de posicoes do tabuleiro */
	//definindo o tabuleiro e suas posições esburacadas
	int tabuleiro[8][8];
	
	int i, j;
	for (i = 0; i< 8; i++){
		for(j=0;j<8; j++){
			tabuleiro[i][j] = 1;
		}
	}
	tabuleiro[3][1] = 0;
	tabuleiro[3][2] = 0;
	tabuleiro[2][5] = 0;
	tabuleiro[5][4] = 0;
	
	//guardando dados refentes a posição inicial do cavalo
	int x = 4, y = 3;
	
	//input dos movimentos do cavalo
	int N;
	scanf("%d", &N);	
	
	
	int movimentos[N];
	
	for (i=0; i<N; i++){
		scanf("%d", &movimentos[i]);
	}
	
	//atribuindo valor aos saltos do cavalo
	
	for (i=0; i<N; i++){
		//caso a posção ATUAL x,y do cavalo seja pertencente ao tabuleiro e não esburacada (começando em (4,3))
		if(tabuleiro[x][y] == 1){
			numMovimentos++;
			if(movimentos[i] == 1){
				y+=2;
				x++;
			}
			
			else if(movimentos[i] == 2){
				y++;
				x+=2;
			}
			
			else if(movimentos[i] == 3){
				y--;
				x+=2;
			}
			
			else if(movimentos[i] == 4){
				y-=2;
				x++;
			}
			
			else if(movimentos[i] == 5){
				y-=2;
				x--;
			}
			
			else if(movimentos[i] == 6){
				y--;
				x-=2;
			}
			
			else if(movimentos[i] == 7){
				y++;
				x-=2;
			}
			
			else if(movimentos[i] == 8){
				y+=2;
				x--;
			}
		}
		else{
			//caso encontre um buraco ou saia do tabuleiro
			return numMovimentos;
		}
	}
	//fim da tragetória
	return numMovimentos;
}
int main(){
	printf("%d", calculaMovimento());
}
