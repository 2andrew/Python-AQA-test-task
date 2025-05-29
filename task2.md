> On the Main page of https://www.hepsiburada.com/ you can see the different Recommendations section with different products. \
> These sections are also shown on Product Detail and Cart pages. \
> What are these product suggestions, what is the rule
for listing these products and showing them to the user? \
> Full analysis is expected here.

Let's inspect HTML body for main page. \
After some time I noticed this section repeats a few times:
> //*[@data-test-id='Recommendation-title']

<pre>
Selected from popular products (Popüler ürünlerden seçtik)
Most Advantageous Products (En Avantajlı Ürünler)
Super Price, Super Offer (Süper Fiyat, Süper Teklif)
Everyone is after these products (Herkes bu ürünlerin peşinde)
Nutritional Supplements & Vitamins (Besin (Gıda) Takviyeleri & Vitaminler)
Camping & Camp Equipment (Kamp & Kampçılık Malzemeleri)
Food Preparation (Yemek Hazırlama)
Bicycle (Bisiklet)
Special discounts on popular categories (Popüler kategorilere özel indirimler)
Bestsellers in daily needs (Günlük ihtiyaçlarda çok satanlar)
Currently Trending (Şu an çok bakılıyor)
Bestsellers of the Week (Haftanın çok satanları)
Premium Offers (Premium fırsatları)
Bestsellers in daily needs (Günlük ihtiyaçlarda çok satanlar)
Special discounts on popular categories (Popüler kategorilere özel indirimler)
</pre>

Let's refresh the page and check sections again

<pre>
Selected from popular products (Popüler ürünlerden seçtik)
Most Advantageous Products (En Avantajlı Ürünler)
Super Price, Super Offer (Süper Fiyat, Süper Teklif)
Everyone is after these products (Herkes bu ürünlerin peşinde)
Car Accessories (Oto Aksesuar Ürünleri)
Cooking (Pişirme)
Sports Categories (Spor Branşları)
Women (Kadın)
Special discounts on popular categories (Popüler kategorilere özel indirimler)
Bestsellers in daily needs (Günlük ihtiyaçlarda çok satanlar)
Currently Trending (Şu an çok bakılıyor)
Bestsellers of the Week (Haftanın çok satanları)
Premium Offers (Premium fırsatları)
</pre>

Some of the sections are not visible on initial page load.\
When I scroll down - I see network requests like this: \
> https://hydra-home-api.hepsiburada.com/api/v1/home/web/view/web_homepage/Recommendation-13?anonymousId=1acff007-d926-4d36-aab4-287da3cac45b&jwt&tenant&userInfo

Let's inspect payload. \
I see that all information about products in section "Recommendation-13" is fully available in response for this request.
<pre>{
    "messages": null,
    "result": [
        {
            "componentKey": "Recommendation-13",
            "type": "Recommendation",
            "data": {
                "placementId": "home_page.dynamic-web-rank29",
                "products": [
                    {
                        "productId": "HB00000C4AQE",
                        "sku": "HBV00000C4AQF",
                        "name": "Binbir Gece Masalları - Antoine Galland",
                        "brandName": "",
                        "discountRate": 8,
                        "discountRateDisplay": "%8",
                        "price": {
                            "value": 32,
                            "currency": "TL",
                            "displayValue": "32,00"
                        },
                        "originalPrice": {
                            "value": 34.9,
                            "currency": "TL",
                            "displayValue": "34,90"
                        },
                        "imageUrl": "https://productimages.hepsiburada.net/s/777/{size}/110001033948198.jpg",
                        "listingId": "d3574f4d-08ae-4b89-8159-3da365e77777",
                        "merchantName": "Hepsiburada",
                        "merchantId": "e750130c-d0ff-469f-8767-66a63af8ea0c",
                        "mainCategoryId": "",
                        "marketPrice": 0,
                        "productUrl": "https://www.hepsiburada.com/binbir-gece-masallari-antoine-galland-p-HBV00000C4AQF",
                        "customerReviewScore": 4.7,
                        "customerReviewCount": 182,
                        "categoryHierarchy": null,
                        "categorizedLabels": {
                            "incentiveToBuy": [
                                {
                                    "imageUrl": "https://images.hepsiburada.net/banners/s/1/105-104/IMAGE-BADGE-CokAvantajli133710426430267271.png",
                                    "badgeImageUrl": "https://images.hepsiburada.net/banners/s/1/105-104/IMAGE-BADGE-CokAvantajli133710426430267271.png",
                                    "tagName": "cok-avantajli-fiyatlar",
                                    "order": 2
                                }
                            ],
                            "valueAddedService": null,
                            "campaign": null
                        },
                        "reasonDetails": "",
                        "reasonCode": "",
                        "isAdProduct": false
                    }
                ]
            }
        }
    ]
}</pre>
____________________________
After doing the same steps a few times, I can see some patterns for the main page:
1. Some sections are always visible to the user:
<pre>
Selected from popular products (Popüler ürünlerden seçtik)
Most Advantageous Products (En Avantajlı Ürünler)
Super Price, Super Offer (Süper Fiyat, Süper Teklif)
Everyone is after these products (Herkes bu ürünlerin peşinde)
</pre>
2. Other sections appear randomly.
3. The number of sections can be different. I usually see 13–15 sections
4. Products that are already in the cart can still be visible in recommendations
5. Sections have up to 20 products (6 are visible on desktop, and other ones are available using carousel mode)
6. The order of products can change (after page refresh or actions like clearing localstorage). 
7. Site use tracking ids like this:
> leo = {anon_id: "01970d3c-97b3-7d1e-923f-2d09f15ce9ad"}
8. Removal of tracking ids/other properties will lead to a situation when Backend will recognize you like a new user and recommendations logic will "go to default mode"
9. Opening site from different locations/countries (VPN or real) doesn't affect categories and product recommendations
10. Opening site from different browsers/screen size/mobile devices doesn't affect categories and product recommendations
____________________________
Let's check the card page now with the similar steps:\
11. After adding any product to the cart, it shows the next sections:
<pre>
Frequently Bought Together (Sıklıkla birlikte alınanlar)
Recommended Sponsored Products (Önerilen reklamlı ürünler)
</pre>
12. Sometimes when I add products from categories that are not connected to each other, like food+bicycle+sneakers — I can see only one section:
<pre>
Recommended Sponsored Products (Önerilen reklamlı ürünler)
</pre>
Options 5–10 from a previous list are working the same way here (except one thing—5 products visible instead of 6 by default)
____________________________
Let's check the product page now with the similar steps:\
13. I see next sections and usually they're present for all products:
<pre>
Recommended Sponsored Products (Önerilen reklamlı ürünler)
You Might Also Be Interested in These (Bunlar da ilgini çekebilir)
Customers Who Viewed This Also Bought (Buna bakanların aldıkları)
Frequently Bought Together (Birlikte alınanlar)
Everyone is Looking at These (Herkes bunlara bakıyor)
Selected from Popular Products (Popüler ürünlerden seçtik)
</pre>
14. Some sections might not be present for some products or some other categories might be visible:
<pre>
You Can Also Check Out These Products (Bu ürünleri de inceleyebilirsin)
</pre>
Options 5–10 from a first list are working the same way here (except one thing—7 products visible instead of 6 by default)
