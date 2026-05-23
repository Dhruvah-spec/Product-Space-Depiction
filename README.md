# Product-Space-Description
The product space is a network that connects products that are believed to require similar kind of knowledge to create, based on the probability of the products being exported in tandem. The idea here is that countries would find it easier to diversify into making products that require similar skills/knowledge to the ones that they already make and so mapping the relatedness between products gives a clue about some possible development paths. It is one of the conceptual tools used in the field of economic complexity for the purpose of analyzing economic development. Studies in this field have noted that the product space contains a core-periphery structure, where the core consists of densely connected products like machinery and chemicals and the periphery contains product like agricultural goods and raw minerals. This study aims to verify these findings by reproducing the product space from scratch using export data. 

# Methodology
To compute the product space, the first step will be to calculate the revealed comparative advantage (RCA) for exports of all products from all countries for the selected year. RCA is given by the formula: RCA〖i,j〗_ =  ((X〖_ij〗)/(X〖_wj〗))/((X〖_i〗)/(X〖_w〗)) , where Xij refers to exports of product i from country j, Xwj refers total exports w from country j, Xi refers to world exports of product i and Xw refers to total world exports. This export data will be sourced from the Altas of Economic Complexity Database as per 4-digit HS classifications of products. These RCA values are then used to calculate a measure called proximity which gives the likelihood of a pair of products being exported together, based on the number of countries that export these products with an RCA > 1. 


The formula for the proximity of a pair of products is: ϕi,j=min⁡(P(RCAi>1∣RCAj>1), P(RCAj>1∣RCAi>1)), where 
P(RCAi>1∣RCAj>1)=
(No of countries that export both product i and product j with RCA>1)/(No of countries that export product j with RCA>1)  and 
P(RCAj>1∣RCAi>1)=(No of countries that export both product i and product j with RCA>1)/(No of countries that export product i with RCA>1)
The minimum of these conditional probabilities is taken as the proximity measure for a pair of products to avoid overestimating the relatedness between two products. For example, if there is a high likelihood for countries that export i to also export j, but there isn’t a high likelihood for countries that export j to also export i, taking the minimum ensures that the products won’t be strongly related. Thus, for there to be a strong proximity between i and j, both conditional probabilities must be high. Once these pair-wise proximities are obtained for all products, they can be used to construct the product space network where nodes would represent products and links would represent the proximities between them. 


	​



