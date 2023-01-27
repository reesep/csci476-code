#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/wait.h>  // because man waitpid() said we'd need this

int main(void) {
    int pid;

    pid = fork();
    if (0 == pid) {
        // I'm the child
        printf("Hi, I'm the child.\n");
      
        char *name[2];
        name[0] = "./hello"; //assuming we have a compiled executable named "./hello"
        name[1] = NULL;
        execve(name[0], name, NULL);
      
        _exit(0); 
    }
    sleep(1);
    printf("I'm the parent. My child has pid %d\n", pid);

    return 0;
}
