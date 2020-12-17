// From: http://beej.us/guide/bgipc/output/html/multipage/mq.html
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>

struct my_msgbuf
{
    long mtype;
    char mtext[200];
};

int main(int argc, char *args[])
{
    struct my_msgbuf buf;
    int msqid;
    key_t key;

    if (argc != 2)
    {
        printf("invalid amount of arguments");
        exit(1);
    }
    if (atoi(args[1]) == 0)
    {
        printf("Invalid queue ID");
        exit(1);
    }

    key = atoi(args[1]);
    /*
    if ((key = ftok("kirk.c", 'B')) == -1) {  // same key as kirk.c
        perror("ftok");
        exit(1);
    }
*/

    if ((msqid = msgget(key, 0644)) == -1)
    { /* connect to the queue */
        perror("msgget");
        exit(1);
    }

    printf("spock: ready to receive messages, captain.\n");

    for (;;)
    { /* Spock never quits! */
        if (msgrcv(msqid, &buf, sizeof(buf.mtext), 0, 0) == -1)
        {
            perror("msgrcv");
            exit(1);
        }
        printf("spock: \"%s\"\n", buf.mtext);
    }

    return 0;
}
