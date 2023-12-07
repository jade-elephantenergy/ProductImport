Stripe.apiKey = "pk_live_51Itf0iBfPYcjROShoTxAJMuKSiALPmBi1MgtLxub6UkXZ2Sos884Sy6E0R221dIQyT5ZFDi5ywz4kIKMxmIdag2c00GmcepI6B";

ProductCreateParams params =
  ProductCreateParams.builder().setName(name).build();

Product product = Product.create(params);
