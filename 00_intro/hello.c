#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>


int main(void) {
    
  printf("Hello from another C progam!\n");
  for(int i = 0; i < 15; i++){
    
    printf("%d\n",i);
    sleep(1);
  }
  
}
