class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        result = 0
        distance = {'P':0,'M':0,"G":0} # M P G distance
        travel = [0] + travel
        i = 0
        for trash in garbage:
            collected = set()
            for key in distance:
                distance[key]+=travel[i]
            for material in trash:
                if material in collected:
                    result+=1   #1 minute to collect if already collected
                else:
                    result+= 1+distance[material]   #1 minute + travelled distance
                    distance[material] = 0
                collected.add(material)
            i+=1
        return result

