#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <pwd.h>

#define CMDMAXLGTH 4096

// glados is uid 1003
#define SETUIDUSER 1003 

#define SUBMIT "/home/glados/submit.pl"
#define GRADE "/usr/bin/python /home/glados/grade.py"


void doSubmission(int argc, char** argv) {
   char buf[CMDMAXLGTH];
   char *p = buf;
   int i=1;

   memset (buf, 0, sizeof(buf));
   p += sprintf(p, " %s", SUBMIT);
   while (argv[i]) {
      p += sprintf(p, " %s", argv[i++]);
   }

   system(buf);
}


void doGrading(int argc, char** argv) {
   char buf[CMDMAXLGTH];
   char *p = buf;

   struct passwd *pwdstruct = getpwuid(getuid());
   char *username = pwdstruct->pw_name;

   memset(buf, 0, sizeof(buf));
   p += sprintf(p, " %s", GRADE);
   p += sprintf(p, " %s", username);

   // just need the username and the project name
   p += sprintf(p, " %s", argv[1]);
   
   sprintf(p, " | tee /home/glados/log/%s-%s.txt", username, argv[1]);
   system(buf);
}


int main(int argc, char **argv) {
   doSubmission(argc, argv);

   setegid(SETUIDUSER);
   seteuid(SETUIDUSER);

   doGrading(argc, argv);

   return 0;
}
