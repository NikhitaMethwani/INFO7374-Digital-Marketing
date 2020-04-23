import pandas as pd


def rfm_score(uid):
    user = pd.read_csv('s3://admfinalproject0801/user_details.csv')
    rfm = pd.read_csv('s3://admfinalproject0801/customer_segmented.csv')
    promotion = pd.read_csv('s3://admfinalproject0801/promotion.csv')

    promotion_det = []
    user_df = pd.DataFrame(user)
    rfm = pd.DataFrame(rfm)
    promotion = pd.DataFrame(promotion)
    user_merge = user_df.merge(rfm, on='user_id')
    user_det = user_merge[user_merge["user_id"] == uid]
    if user_det["Age"].shape[0] == 0:
        segment = "New User"
        promotion_det.append(promotion[promotion['promotionid'] == 1])
        promo = promotion_det[0].promotion_offer
    else:
        a = user_det['RFMScore']
        # promotion_det = []
        if a.values[0] <= 244:
            segment = "Beginner"
            promotion_det.append(promotion[promotion['promotionid'] == 1])
        if a.values[0] > 244 and a.values[0] < 344:
            segment = "Gold"
            promotion_det.append(promotion[promotion['promotionid'] == 2])
        if a.values[0] >= 344:
            segment = "Platinium"
            promotion_det.append(promotion[promotion['promotionid'] == 3])
        promo = promotion_det[0].promotion_offer
        # promo[1]
    promo = pd.DataFrame(promo)
    return (segment, promo)
