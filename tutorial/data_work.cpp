#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include "sqlite3.h"
#include <queue>
#pragma comment(lib, "sqlite3.lib")

using namespace std;

//13 - 17
map<string, int> mp[10];

int getYearId(string year) {
    if (year == "2013") return 0;
    else if (year == "2014") return 1;
    else if (year == "2015") return 2;
    else if (year == "2016") return 3;
    else if (year == "2017") return 4;
    else if (year == "2018") return 5;
    else return 6;
}

void Get_from_sql() {
    sqlite3* db;
    int nResult = sqlite3_open("data.db", &db);
    if (nResult != SQLITE_OK)
    {
        cout << "open fail " << sqlite3_errmsg(db) << endl;
        return;
    }
    else
    {
        cout << "open succeed" << endl;
    }
    
    char* errmsg;
    string strSql = "select * from askdata";
    //nResult = sqlite3_exec(db,strSql.c_str(),callback,NULL,&errmsg);
    char** pResult;
    int nRow;
    int nCol;
    nResult = sqlite3_get_table(db, strSql.c_str(), &pResult, &nRow, &nCol, &errmsg);
    
    if (nResult != SQLITE_OK)
    {
        sqlite3_close(db);
        cout << errmsg << endl;
        sqlite3_free(errmsg);
        return;
    }
    
    for (int i = 0; i<10; i++)
        mp[i].clear();
    string strOut;
    int nIndex = nCol;
    cout << "analysing"<<endl;		//show detail
    for (int i = 0; i<nRow; i++)
    {
        if (i % 1000 == 0)
            cout << ".";
        string date;
        string year;
        string tag;
        int year_id;
        for (int j = 0; j<nCol; j++)
        {
            //    strOut+=pResult[j];
            //    strOut+=":";
            //    strOut+=pResult[nIndex];
            //    strOut+="\n";
            //    ++nIndex;
            if (j == 0) {
                date = pResult[nIndex];
                year = date.substr(0, 4);
            }
            else {
                tag = pResult[nIndex];
                year_id = getYearId(year);
                mp[year_id][tag]++;
            }
            ++nIndex;
        }
    }
    cout << "done" << endl;
    sqlite3_free_table(pResult);
    //   cout<<strOut<<endl;
    sqlite3_close(db);
}

const int year[] = { 2013,2014,2015,2016,2017,2018 };
const string years[] = { "2013","2014","2015","2016","2017","2018" };


priority_queue<pair<int, string> ,vector<pair<int, string>> ,greater<pair<int, string>> > q[10] ;

void Work_data() {
    ofstream out;
    
    cout << "write in csv" << endl;
    for (int i = 2; i<5; i++) {
        out.open(years[i]+"out.csv");
        out << "tag,cnt" << endl;
        //if open
        cout << years[i];  //show detail
        
        int tag_cnt = (int)mp[i].size();
        
        //out << year[i] << " year have " << tag_cnt << "tags" << endl;
        //printf("%d year have %d tags\n", year[i], tag_cnt);
        
        for (auto it : mp[i]) {
            string tag = it.first;
            if (tag=="0") continue;
            int cnt = it.second;
           // out << tag << "," << cnt << endl;
            if (q[i].size()< 20){
                q[i].push(make_pair(cnt,tag));
            }
            else{
                pair<int, string> tmp = q[i].top();
                if (cnt > tmp.first || (cnt == tmp.first && tag<tmp.second)){
                    q[i].pop();
                    q[i].push(make_pair(cnt,tag));
                }
            }
        }
        while (!q[i].empty()){
            pair<int, string> tmp = q[i].top();
            out << tmp.second << "," << tmp.first << endl;
            q[i].pop();
        }
        cout << "..........done" << endl;
        out.close();

    }
    //fclose(stdout);
}
int main() {
    Get_from_sql();
    Work_data();
    system("pause");
    return 0;
}
