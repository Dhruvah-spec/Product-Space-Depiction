# Product-Space-Depiction
The product space is a network that connects products that are believed to require similar kind of knowledge to create, based on the probability of the products being exported in tandem. The idea here is that countries would find it easier to diversify into making products that require similar skills/knowledge to the ones that they already make and so mapping the relatedness between products gives a clue about some possible development paths. It is one of the conceptual tools used in the field of economic complexity for the purpose of analyzing economic development. Studies in this field have noted that the product space contains a core-periphery structure, where the core consists of densely connected products like machinery and chemicals and the periphery contains product like agricultural goods and raw minerals. This study aims to verify these findings by reproducing the product space from scratch using export data. 

## Methodology
To compute the product space, the first step is to calculate the **Revealed Comparative Advantage (RCA)** for exports of all products from all countries for a selected year.

## Revealed Comparative Advantage (RCA)

The RCA formula is given by:

```math
RCA_{i,j} = \frac{\left(\frac{X_{ij}}{X_{wj}}\right)}{\left(\frac{X_i}{X_w}\right)}
```

Where:

- `Xij` = exports of product *i* from country *j*
- `Xwj` = total exports of country *j*
- `Xi` = total world exports of product *i*
- `Xw` = total world exports

Export data is sourced from the **World Integrated Trade Solution (WITS)** database using **4-digit HS product classifications**.

The RCA values are then used to calculate **proximity**, which measures the likelihood that two products are exported together. This is based on the number of countries exporting both products with `RCA > 1`.

---

# Product Proximity

The proximity between a pair of products is defined as:

```math
\phi_{i,j} = \min \left( P(RCA_i > 1 \mid RCA_j > 1),\; P(RCA_j > 1 \mid RCA_i > 1) \right)
```

## Conditional Probabilities

### Probability of exporting product *i* given export of product *j*

```math
P(RCA_i > 1 \mid RCA_j > 1) =
\frac{
\text{Number of countries exporting both } i \text{ and } j \text{ with } RCA > 1
}{
\text{Number of countries exporting } j \text{ with } RCA > 1
}
```

### Probability of exporting product *j* given export of product *i*

```math
P(RCA_j > 1 \mid RCA_i > 1) =
\frac{
\text{Number of countries exporting both } i \text{ and } j \text{ with } RCA > 1
}{
\text{Number of countries exporting } i \text{ with } RCA > 1
}
```

	​



