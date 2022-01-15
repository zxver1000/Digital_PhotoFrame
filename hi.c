#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>

static sem_t sem_one;
static sem_t sem_two;
static int num, x;

void *input(void *);
void *accu(void *);

int main(int argc, char **argv) 
{
    pthread_t id_t1, id_t2;
    if(sem_init(&sem_one, 0, 1) != 0) {
        perror("sem init");
        return -1;
    }
    if(sem_init(&sem_two, 0, 0) != 0) {
        perror("sem init");
        return -1;
    }
    
    if(pthread_create(&id_t1, NULL, input, NULL) != 0) {
        perror("pthread create");
        return -1;
    }
    if(pthread_create(&id_t2, NULL, accu, NULL) != 0) {
        perror("pthread create");
        return -1;
    }

    if(pthread_join(id_t1, NULL) != 0) {
        perror("pthread_join");
        return -1;
    }   
    if(pthread_join(id_t2, NULL) != 0) {
        perror("pthread_join");
        return -1;
    }   
    
    printf("num=%d\n", num);
    return 0;
}

void *input(void *arg)
{
    for(int i=0; i<5; i++) {
        sem_wait(&sem_one);
        scanf("%d", &x);
        sem_post(&sem_two);
    }
    return NULL;
}

void *accu(void *arg)
{
    for(int i=0; i<5; i++) {
        sem_wait(&sem_two);
        num += x;
        sem_post(&sem_one);
    }
    return NULL;
}