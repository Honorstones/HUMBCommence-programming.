#include<iostream>
#include<fstream>

using namespace std;
int main(){
  ofstream write("prime.txt");
  write.open();
  write<<"Prime is my first cpp program on GitHub";
  return 0;
    
}
