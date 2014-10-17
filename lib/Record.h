#ifndef RECORD_H
#define RECORD_H 

#include <string>
#include <unordered_map>

using namespace std;

struct MatchRecord{
	int win;
	int loss;
	int fightCount;
	string opponentName;
	string opponentDeckName;
};

class Record
{
public:
	Record(string deckName);
	~Record();
	void printRecord() const;
	void printRecord(string opponentName) const;
	void findHistoryAgainst(string opponent) const;
	bool recordExists(string opponentName) const;
	void updateRecord(string opponentName, int result);
	void createNewRecord(string opponentName, string opponentDeckName, int result);

private:
	string deckName;
	int overallWins;
	int overallLoss;
	unordered_map<string, MatchRecord> history_map;
	
};
#endif