#include <stdio.h>

int ary[1000], dp1[1000], dp2[1000];
int max(int a, int b);

int main(void) {
	int size;
	scanf("%d", &size);
	for(int i=0; i<size; i++){
		scanf("%d", &ary[i]);
	}
	//1. 앞에서부터 가장 긴 증가 부분 수열 찾기
	for(int i=0; i<size; i++){
		dp1[i]=1;
		for(int j=0; j<i; j++){
			if(ary[i]>ary[j]){
				dp1[i] = max(dp1[i], dp1[j]+1);
			}
		}
	}
	//2. 뒤에서부터 가장 긴 증가 부분 수열 찾기 
	for(int i=size-1; i>=0; i--){
		dp2[i]=1;
		for(int j=size-1; j>i; j--){
			if(ary[i]>ary[j]){
				dp2[i] = max(dp2[i], dp2[j]+1);
			}
		}
	}
	//3. dp1[i]+dp2[i] 값들 중 최댓값 찾기
	int result=0;
	for(int i=0; i<size; i++){
		result = max(result, dp1[i]+dp2[i]-1);//i번째 원소는 두번 겹침
	}
	printf("%d\n", result);
	return 0;
}

int max(int a, int b){
	if (a>b) return a;
	else return b;
}