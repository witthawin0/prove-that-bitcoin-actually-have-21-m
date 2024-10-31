height = 0  # ตัวแปรนี้แทนความสูงของบล็อกปัจจุบัน
nSubsidyHalvingInterval = 210000  # จำนวนบล็อกที่ขุดได้ก่อนที่จะมีการ Halving ครั้งหนึ่ง
COIN = 100000000
TotalSupply = 0  # ตัวแปรนี้แทนยอดเหรียญสะสมทั้งหมด

while True:
    # คำนวณรอบของการ Halving โดยแบ่งจำนวนบล็อกที่ขุดได้ด้วย 210000
    # ซึ่งจะได้ผลลัพธ์เป็นจำนวนรอบ Halving เช่น รอบแรก (0) ถึงรอบ 64 (สิ้นสุด)
    halving = int(height / nSubsidyHalvingInterval) 

    # เมื่อถึง Halving รอบที่ 64 ค่ารางวัล (subsidy) จะเท่ากับศูนย์
    # เนื่องจากบล็อกที่ขุดได้จะไม่ให้รางวัลเป็น Bitcoin อีกต่อไป
    if halving >= 64:
        nSubsidy = 0  # การขุดจะไม่ให้รางวัลใหม่ แต่ยังมีค่าธรรมเนียมจากการโอน
    
    else:
        # คำนวณรางวัลในแต่ละบล็อก โดยเริ่มต้นที่ 50 BTC
        # >> halving เป็นการลดครึ่งนึงทุก ๆ รอบ Halving
        nSubsidy = (50 * COIN) >> halving  # หน่วยของ 1 BTC = 100000000 ซาโตชิ
        TotalSupply += nSubsidy  # เพิ่มจำนวนเหรียญที่ขุดได้สะสมในตัวแปร TotalSupply
    
    print(f"Height: {height:,} Blocks, Subsidy: {nSubsidy:,}, Total: {TotalSupply:,}")
    
    # สิ้นสุดการทำงานเมื่อไม่มีรางวัลจากการขุด (เมื่อค่า nSubsidy เท่ากับศูนย์)
    if nSubsidy == 0:
        break

    # เพิ่มจำนวนบล็อก (วนลูปไปบล็อกถัดไป)
    height += 1
