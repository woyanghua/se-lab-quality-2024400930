# before.py - 包含代码坏味道（重复代码、未使用变量、过长函数）
class OrderProcessor:
    def process_online_order(self, items, user):
        # 空订单校验（重复代码）
        if len(items) == 0:
            print("订单为空，无法处理")
            return False
        
        # 计算商品总价（重复代码）
        total = 0
        for item in items:
            total += item["price"] * item["quantity"]
        print(f"计算总价：{total}")
        
        # VIP折扣（重复代码）
        if user["is_vip"]:
            total = total * 0.9
            print("VIP折扣已应用")
        
        # 税费计算（重复代码）
        tax_rate = 0.1
        tax = total * tax_rate
        final_price = total + tax
        print(f"税费：{tax}，最终价格：{final_price}")
        
        print(f"线上订单处理完成，总价：{final_price}")
        return True

    def process_offline_order(self, items, user):
        # 和process_online_order 100%重复的代码块（CodeQL必识别）
        if len(items) == 0:
            print("订单为空，无法处理")
            return False
        
        total = 0
        for item in items:
            total += item["price"] * item["quantity"]
        print(f"计算总价：{total}")
        
        if user["is_vip"]:
            total = total * 0.9
            print("VIP折扣已应用")
        
        tax_rate = 0.1
        tax = total * tax_rate
        final_price = total + tax
        print(f"税费：{tax}，最终价格：{final_price}")
        
        print(f"线下订单处理完成，总价：{final_price}")
        return True

# 多个未使用变量（CodeQL必识别）
unused_var1 = 100
unused_var2 = "这是未使用的变量2"
unused_var3 = [1,2,3,4,5]

# 未使用的函数
def unused_function():
    print("这个函数定义了但从未被调用")

if __name__ == "__main__":
    processor = OrderProcessor()
    test_items = [{"price": 100, "quantity": 2}, {"price": 50, "quantity": 1}]
    test_user = {"is_vip": True}
    processor.process_online_order(test_items, test_user)
    processor.process_offline_order(test_items, test_user)
