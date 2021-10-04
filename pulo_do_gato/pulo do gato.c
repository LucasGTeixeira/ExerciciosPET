#include <stdio.h>
#include <stdlib.h>
int pulo_do_gato(){
	
	//inputando a quantidade de Lajotas
	int C;
	int i = 0;
	do{
		scanf("%d", &C);
	}while(C < 1 || C > 10000);
	
	//criando a lista de tamanho C 
	//para armazenar as cores das lajotas
	int Lajotas[C];
	
	for (i=0; i<C; i++){
		scanf("%d", &Lajotas[i]);
	}
	//calculando os pulos
	i = 0;
	int cont = 0;
	while (i < C-1){
		if (Lajotas[i+2] == 1){
			cont = cont + 1;
			i += 2;
		}
		else if (Lajotas[i+1] == 1 && Lajotas[i+2] == 0){
			cont = cont + 1;
			i += 1;
		}
		else{
			return -1;
		}	
	}
	return cont;
}
int main(){
	printf("%d", pulo_do_gato());
}
