#include <iostream>
using namespace std;

int tq = 5;
int pid  = 0;
int at = 1;
int bt = 2;
int rt = 3;
int st = 4;
int et = 5;
int wt = 6;
int tat = 7;
	

int main(){	
	int processes[5][8] = {{0,0,15},{1,0,5},{2,0,30},{3,0,10},{4,0,20}};
	
	for(int i = 0; i < 5; i++){
		processes[i][st] = i*tq;			//start time
		processes[i][rt] = processes[i][bt];
		//processes[i][et] = 0;
		//processes[i][wt] = 0;
		//processes[i][tat] = 0;
	}
	
	//End time
	int ct = 0;
	for(int i = 0; i < 6; i++){
		for(int j = 0; j < 5; j++){
			if(processes[j][rt]>0){
				ct += tq;
				processes[j][rt] = processes[j][rt] - tq;
				
				if(processes[j][rt] == 0){
					processes[j][et] = ct;
				}
			}
		}
	}
	
	//wt and tat
	for(int i = 0; i < 5; i++){
		processes[i][wt] = processes[i][et] - processes[i][bt];
		processes[i][tat] = processes[i][wt] + processes[i][bt];
	}	
	
	cout<<"PID\tAT\tBT\tRT\tST\tET\tWT\tTAT\n";
	for(int i = 0; i < 5; i++){
		for(int j = 0; j < 8; j++){
			cout<<processes[i][j]<<"\t";
		}
		cout<<endl;
	}	
	return 0;
}
