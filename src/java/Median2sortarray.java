import java.util.List;
import java.util.Collections;
import java.util.Arrays;
import java.util.ArrayList;

public class Median2sortarray {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
	List<Integer> l = new ArrayList<Integer>();
	for (int i =0; i<nums1.length; i++)
	    l.add(nums1[i]);
	for (int i=0; i<nums2.length; i++)
	    l.add(nums2[i]);
        Collections.sort(l);
        if (l.size() % 2 == 1)
            return l.get(l.size()/2);
        else
            return ((int)l.get(l.size()/2) + (int)l.get(l.size()/2-1) ) / 2.0;        
    }

    public static void main(String argv[]){
	int[] a = {1,2,3,4,5};
	int[] b = {6,7,8,9,10};
	Median2sortarray m = new Median2sortarray();
	for (int i = 0; i< a.length; i++)
	    System.out.println(a[i]);
        for (int i = 0; i< b.length; i++)
            System.out.println(b[i]);
	System.out.println(m.findMedianSortedArrays(a, b));
    }
}
