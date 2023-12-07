Stripe.apiKey = "sk_test_51Itf0iBfPYcjROShi56UtBWV7LSOL8NXIdOBIuomUYsBURIBIVTLJDaytHADabDx4O60w0HNEr68Vc0sdbA6Y9Jr00lH37G4R6";

ProductCreateParams params =
  ProductCreateParams.builder().setName("Gold Plan").build();

Product product = Product.create(params);
