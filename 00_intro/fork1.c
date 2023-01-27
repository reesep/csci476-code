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
        _exit(0); // what happens if we don't have this?
    }
    sleep(1);
    printf("I'm the parent");

    return 0;
}
