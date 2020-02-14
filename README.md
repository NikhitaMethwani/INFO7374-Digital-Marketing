# INFO7374-Digital-Marketing
Digital Marketing 

Open Payment CMS Marketing Analysis:

Open Payments is a national transparency program that collects and publishes information about financial relationships between the health care industry (i.e. drug and device companies) and providers (i.e. physicians and teaching hospitals). These relationships may involve payments to providers for things such as research, meals, travel, gifts, or speaking fees. One of the ways that the Centers for Medicare & Medicaid Services (CMS) provides data to the public is through this search tool, which allows the public to search for physicians and teaching hospitals receiving payments, as well as companies that have made payments.

The purpose of the program is to provide the public with a more transparent healthcare system. All information available on the Open Payments database is open to personal interpretation and if there are questions about the data, healthcare consumers should speak directly to the healthcare provider for a better understanding. 

Datasets:
Research Dataset : This dataset consists of the payments done by manufacturers/GPOs in the research department ( Teaching Hospitals / Physicians ) based across states.

General Dataset : This dataset gives the general payments done on testing the products by Teaching Hospitals / Physicians 
The payments are provided based on the physician types(Doctor,Dentists,Osteopathy) & specialities(Allergy Specialist,Heart Specialist,General Practice)

Ownership Dataset : This dataset determines the investment done by the physicians in the manufacturing products (devices,drugs)


Analysis is done on the dataset to do the recommendation , pricing , search and promotion of products to the physicians and the hospitals.


XSV was used to join 3 dataset based on profile IDs of Physicians which gave us a clear  idea of how each physician is getting paid (Payment modes) , for what service ( Research/General) and in how many manufacturers he has invested in.

Tools such as python - pandas was used for cleaning the data such as correcting/removing null values and doing the initial statistics of data.

Salesforce was used to do the visualization and create various dashboards to understand the analysis such as:
Competitive analysis : indicates the investment done by each manufacturer in each state on same physician types/categories,this helps the manufacturer to target the physicians of same category in the states where they are not targeted.

Pricing : It determines the top manufacturers and their investment in the products and product categories.
The high demand of physician specialities based on their products can be targeted.

Resource Allocation: The physicians who invest in the manufacturers are targeted based on the state

More details : https://codelabs-preview.appspot.com/?file_id=1Y1vXECVH8DN2NaWSV29jIx_m_K0i-OeyWpfOUJNBSKQ#0
