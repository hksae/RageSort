import java.util.*;

public class RageSort {
    
    public static List<Integer> bitRadixSort(List<Integer> data) {
        return bitRadixSort(data, 8);
    }
    
    public static List<Integer> bitRadixSort(List<Integer> data, int radixBits) {
        if (data.size() < 2) {
            return new ArrayList<>(data);
        }
        
        List<Integer> zeros = new ArrayList<>();
        List<Integer> nonZeros = new ArrayList<>();
        
        for (int x : data) {
            if (x == 0) {
                zeros.add(x);
            } else {
                nonZeros.add(x);
            }
        }
        
        if (nonZeros.isEmpty()) {
            return zeros;
        }
        
        int maxBits = 0;
        for (int x : nonZeros) {
            int length = Integer.toBinaryString(Math.abs(x)).length();
            if (length > maxBits) {
                maxBits = length;
            }
        }
        
        List<List<Integer>> posGroups = new ArrayList<>(maxBits + 1);
        List<List<Integer>> negGroups = new ArrayList<>(maxBits + 1);
        
        for (int i = 0; i <= maxBits; i++) {
            posGroups.add(new ArrayList<>());
            negGroups.add(new ArrayList<>());
        }
        
        for (int x : nonZeros) {
            if (x < 0) {
                negGroups.get(Integer.toBinaryString(Math.abs(x)).length()).add(x);
            } else {
                posGroups.get(Integer.toBinaryString(x).length()).add(x);
            }
        }
        
        List<Integer> sortedResult = new ArrayList<>();
        
        for (int i = maxBits; i > 0; i--) {
            if (!negGroups.get(i).isEmpty()) {
                List<Integer> absGroup = new ArrayList<>();
                for (int x : negGroups.get(i)) {
                    absGroup.add(Math.abs(x));
                }
                List<Integer> sortedAbs = coreSort(absGroup, i, radixBits);
                for (int val : sortedAbs) {
                    sortedResult.add(-val);
                }
            }
        }
        
        sortedResult.addAll(zeros);
        
        for (int i = 0; i <= maxBits; i++) {
            if (!posGroups.get(i).isEmpty()) {
                sortedResult.addAll(coreSort(posGroups.get(i), i, radixBits));
            }
        }
        
        return sortedResult;
    }
    
    private static List<Integer> coreSort(List<Integer> subset, int bitCount, int step) {
        if (subset.size() < 2 || bitCount <= 0) {
            return new ArrayList<>(subset);
        }
        
        int highBit = 1 << (bitCount - 1);
        List<Integer> workingData = new ArrayList<>();
        for (int num : subset) {
            workingData.add(num ^ highBit);
        }
        
        int numPasses = (Math.max(0, bitCount - 1) + step - 1) / step;
        int mask = (1 << step) - 1;
        
        for (int p = 0; p < numPasses; p++) {
            int shift = p * step;
            List<List<Integer>> buckets = new ArrayList<>(1 << step);
            for (int i = 0; i < (1 << step); i++) {
                buckets.add(new ArrayList<>());
            }
            
            for (int num : workingData) {
                int idx = (num >> shift) & mask;
                buckets.get(idx).add(num);
            }
            
            workingData = new ArrayList<>();
            for (List<Integer> bucket : buckets) {
                workingData.addAll(bucket);
            }
        }
        
        List<Integer> result = new ArrayList<>();
        for (int num : workingData) {
            result.add(num ^ highBit);
        }
        
        return result;
    }
    
    public static int[] bitRadixSort(int[] data) {
        return bitRadixSort(data, 8);
    }
    
    public static int[] bitRadixSort(int[] data, int radixBits) {
        List<Integer> list = new ArrayList<>();
        for (int x : data) {
            list.add(x);
        }
        List<Integer> sorted = bitRadixSort(list, radixBits);
        int[] result = new int[sorted.size()];
        for (int i = 0; i < sorted.size(); i++) {
            result[i] = sorted.get(i);
        }
        return result;
    }
}