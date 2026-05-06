# after.py - 重构修复后（消除重复代码、未使用变量/函数）
class OrderProcessor:
    # 提取公共逻辑，消除重复代码
    def _calculate_order_price(self, items, user):
        """公共价格计算函数，复用所有订单类型的价格逻辑"""
        if len(items) == 0:
            return None
        
        # 简化总价计算
        total = sum(item["price"] * item["quantity"] for item in items)
        
        # VIP折扣
        if user["is_vip"]:
            total *= 0.9
        
        # 税费计算
        tax_rate = 0.1
        tax = total * tax_rate
        final_price = total + tax
        
        return {
            "total": total,
            "tax": tax,
            "final_price": final_price
        }

    def process_online_order(self, items, user):
        """线上订单处理（仅保留业务逻辑，复用公共计算）"""
        price_info = self._calculate_order_price(items, user)
        if price_info is None:
            print("订单为空，无法处理")
            return False
        
        print(f"计算总价：{price_info['total']}")
        print("VIP折扣已应用" if user["is_vip"] else "")
        print(f"税费：{price_info['tax']}，最终价格：{price_info['final_price']}")
        print(f"线上订单处理完成，总价：{price_info['final_price']}")
        return True

    def process_offline_order(self, items, user):
        """线下订单处理（无重复代码）"""
        price_info = self._calculate_order_price(items, user)
        if price_info is None:
            print("订单为空，无法处理")
            return False
        
        print(f"计算总价：{price_info['total']}")
        print("VIP折扣已应用" if user["is_vip"] else "")
        print(f"税费：{price_info['tax']}，最终价格：{price_info['final_price']}")
        print(f"线下订单处理完成，总价：{price_info['final_price']}")
        return True

if __name__ == "__main__":
    processor = OrderProcessor()
    test_items = [{"price": 100, "quantity": 2}, {"price": 50, "quantity": 1}]
    test_user = {"is_vip": True}
    processor.process_online_order(test_items, test_user)
    processor.process_offline_order(test_items, test_user)
