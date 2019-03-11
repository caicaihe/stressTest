from locust import HttpLocust, TaskSet, task
import json
import time

class WebsiteTasks(TaskSet):
    '''@task(1)    #通过@task()装饰的方法为一个事务，方法的参数用于指定该行为的执行权重，参数越大每次被虚拟用户执行的概率越高，默认为1
    def index(self):
        payload = {"scm":{"type":"Gitlab","authType":"Password","username":"peter","server":"http://192.168.130.29:81","password":"1wonderful"},"cargo":{"projectType":"default","name":"default"},"workerQuota":{"cpuRequests":"0.5","cpuLimits":"1","memoryRequests":"1Gi","memoryLimits":"2Gi"},"alias":"abcd"}
        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "X-Tenant":"devops",
            "Authorization":"Basic YWRtaW46UHdkMTIzNDU2"
        }
        bbb = json.dumps(payload)
        with self.client.post("/workspaces",data=bbb,headers=header,catch_response=True) as response:
            print(response.status_code)
        time.sleep(5)
        self.client.delete("/workspaces/abcd",headers=header)'''

    @task(1)    #通过@task()装饰的方法为一个事务，方法的参数用于指定该行为的执行权重，参数越大每次被虚拟用户执行的概率越高，默认为1
    def index2(self):
        payload = {"scm":{"type":"Gitlab","authType":"Password","username":"peter","server":"http://192.168.130.29:81","password":"1wonderful"},"cargo":{"projectType":"default","name":"default"},"workerQuota":{"cpuRequests":"0.5","cpuLimits":"1","memoryRequests":"1Gi","memoryLimits":"2Gi"},"alias":"ddd"}
        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "X-Tenant":"devops",
            "Authorization":"Basic YWRtaW46UHdkMTIzNDU2"
        }
        bbb = json.dumps(payload)
        with self.client.post("/workspaces",data=bbb,headers=header,catch_response=True) as response:
            print(response.status_code)
            responseJson = response.json()
            print(responseJson['name'])
            kk = responseJson['name']
        time.sleep(5)
        key = "/workspaces"+"/"+kk
        self.client.delete(key,headers=header) 



class WebsiteUser(HttpLocust):
    host     = "http://192.168.129.30:6002/apis/admin.devops.caicloud.io/v1" #被测系统的host，在终端中启动locust时没有指定--host参数时才会用到
    task_set = WebsiteTasks          #TaskSet类，该类定义用户任务信息，必填。这里就是:WebsiteTasks类名,因为该类继承TaskSet；
    min_wait = 5000  #每个用户执行两个任务间隔时间的上下限（毫秒）,具体数值在上下限中随机取值，若不指定默认间隔时间固定为1秒
    max_wait = 15000