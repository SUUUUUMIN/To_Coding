while True:
  try:
    coupon, stamp=map(int,input().split())
    chicken=coupon
    while coupon>=stamp:
      chicken+=coupon//stamp
      coupon=coupon//stamp+coupon%stamp
    print(chicken)
  except:
    break