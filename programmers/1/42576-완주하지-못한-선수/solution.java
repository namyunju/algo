import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();
        // 참여자 명단을 HashMap에 등록
        // 동명이인이 있을 수 있음
        for (String player : participant) {
            map.put(player, map.getOrDefault(player, 0) + 1);
        }
        // 완주자 명단
        for (String player : completion) {
            map.put(player, map.get(player) - 1);
        }
        
        for (String key : map.keySet()) {
            if (map.get(key) != 0) {
                answer = key;
                break;
            }
        }
        return answer;
    }
}