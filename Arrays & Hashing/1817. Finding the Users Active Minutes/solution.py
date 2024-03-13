# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0]*k
        m = {}
        for ID, time in logs:
            if ID in m:
                m[ID].add(time)
            else:
                m[ID] = set([time])

        for key,val in m.items():
            pos = len(val)-1
            answer[pos] += 1
        return answer