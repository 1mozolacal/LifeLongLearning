// From: http://beej.us/guide/bgipc/output/html/multipage/mq.html
/*

3 -- When kirk ended, why did spock also end?
    Spock(any and all running) will end as soon a kirk(a single kirk) is closed because when they read from the mailbox (which will fail) and the function call return -1 which satisfise the if condition which then exits the program.

4 -- Try starting spock first. What "output" does it give? Why?
    It prints out "msgget: No such file or directory". This is because when Spock attempts to connect to the mailbox(doesn't create it with bitwise OR with IPC_CREAT) the mailbox has yet to be created by Kirk. Thus Spock is looking for a mailbox that doesnt exist hence the "No such file or directory".

5 -- Start kirk in one window, then spock in another. Make kirk give some orders. Now try to end spock with CTRL-D. It won't end. Why? End both by sending kirk CTRL-D.
    The reason why Spock does not end on CTRL-D is because CTRL-D is the end of file character which does not get read or used by the Spock program at all. Instead it is in an infinite loop that is just reading from the mailbox. The only reason why Kirk ends on CTRL-D is because kirk.c terminates itself if it reads end of file.

7 -- Any message queues you make will continue to exist until they are explicitly deleted. How does kirk.c and/or spock.c delete the message queue? 
    Normally the kirk.c will delete the message queue when ^D is entered. It does this will the msgctl(msqid, IPC_RMID,NULL) function call.

8 -- What can this tell you about the process scheduling? 
    When I have multiple Spocks open they will receive the messages in a cyclical pattern. This means that blocked processes are kept in a Queue(FIFO).



*/

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
//#include <ctype.h>

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

    //printf("I have %d length  or %d \n", sizeof(args), argc );

    if (argc != 2)
    {
        printf("invalide amount of arguments");
        exit(1);
    }
    if (atoi(args[1]) == 0)
    {
        printf("invalide queue ID");
        exit(1);
    }

    key = atoi(args[1]); //set the key to the number passed in
                         /*
    if ((key = ftok("kirk.c", 'B')) == -1) {
        perror("ftok");
        exit(1);
    }*/

    if ((msqid = msgget(key, 0644 | IPC_CREAT)) == -1)
    {
        perror("msgget");
        exit(1);
    }

    printf("Enter lines of text, ^D to quit:\n");

    buf.mtype = 1; /* we don't really care in this case */

    while (fgets(buf.mtext, sizeof buf.mtext, stdin) != NULL)
    {
        int len = strlen(buf.mtext);

        /* ditch newline at end, if it exists */
        if (buf.mtext[len - 1] == '\n')
            buf.mtext[len - 1] = '\0';

        if (msgsnd(msqid, &buf, len + 1, 0) == -1) /* +1 for '\0' */
            perror("msgsnd");
    }

    if (msgctl(msqid, IPC_RMID, NULL) == -1)
    {
        perror("msgctl");
        exit(1);
    }

    return 0;
}
