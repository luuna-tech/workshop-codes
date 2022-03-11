export interface WebClientItem {
  quantity: Number;
  product: Product;
}

export interface Product {
  id: string;
  name: string;
  baselineRate: Number;
  finalRate: Number;
  image: ProductImage;
}

export interface ProductImage {
  small: string;
}
