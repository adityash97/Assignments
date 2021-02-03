// Every date must be unique
#include<iostream>
#include<map>
using namespace std;

int findValue(char key1 = '0',char key2 = '0'){
    int data = 0;
    // cout << "Key1 " << key1 << "Key2 " << key2 << endl;
     if(key1 == '0' and key2 != '0'){
            data = key2 - '0';
        }else if (key1 != '0' and key2 == '0'){
            data = key1 - '0';
             data *= 10;
        }else{
            int ans1 = key1 - '0';
            int ans2 = key2 -'0';
            data = (ans1*10)+ans2;            
        }
    // cout << "Data : " << data << endl;
    return data;
}
int findMonthCode(int data,int month[]){
    for(int i=0;i<12;i++){
        if(data == i)
            return month[i];
    }
}
int findCenturyCode(int data,map<int,int> &century){
    map<int,int> :: iterator it;
    it = century.find(data);
    if(it != century.end())
        return it->second;
}
string findDay(int data,map<int,string> &day){
    map<int,string> :: iterator it;
    it = day.find(data);
    if(it != day.end())
        return it->second;
}



int main(){
    map<string,int> output;
    map<string,int> D;
    D["2020-01-01"] = 6;
    D["2020-01-04"] = 12;
    D["2020-01-05"] = 14;
    D["2020-01-06"] = 2;
    D["2020-01-07"] = 4;
    map<int,int> Century;
    Century[19] = 0;
    Century[20] = 6;
    Century[21] = 4;
    int Month[] ={-1,1,4,4,0,2,5,0,3,6,1,4,3};
    map<int,string> Day ;
    Day[0] = "Sat";
    Day[1] = "Sun";
    Day[2] = "Mon";
    Day[3] = "Tue";
    Day[4] = "Wed";
    Day[5]= "Thru";
    Day[6] = "Fri";
// ans = a+b+c+d+e
    for(auto &[key,value] : D){
        // cout <<"==>" <<key << endl;
        // cout<< key[8] << key[9] << endl;
        int a = findValue(key[8],key[9]);
        int b = findValue(key[5],key[6]);
        int c = findValue(key[0],key[1]);
        int d = findValue(key[2],key[3]);
        int e = d/4;
        int ans = a+findMonthCode(b,Month)+findCenturyCode(c,Century)+d+e ;
        ans = (ans%7)-1;
        string day = findDay(ans,Day);
        // cout << "Day =" << day << endl;
        output[day] = D[key];
    }

    for(auto &[key,value] : output){
        cout <<key << "=>" <<output[key] << endl;
    }

}