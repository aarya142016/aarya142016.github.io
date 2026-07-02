import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Define the book reviews collection
const bookReviews = defineCollection({
  loader: glob({
    base: './src/content',
    pattern: 'book-reviews/**/*.md'
  }),
  schema: z.object({
    title: z.string(),
    author: z.string(),
    yearRead: z.number(),
    rating: z.number().min(1).max(5),
    genre: z.string().optional(),
    tags: z.array(z.string()).optional(),
    coverImage: z.string().optional(),
    dateRead: z.coerce.date().optional(),
    // Content fields that were in the body
    summary: z.string(),
    learned: z.array(z.string()),
    favoritePart: z.string(),
    recommend: z.string(),
  }),
});

export const collections = {
  'book-reviews': bookReviews,
  'years': defineCollection({
    loader: glob({
      base: './src/content',
      pattern: 'years/**/*.md'
    }),
    schema: z.object({
      title: z.string(),
      grade: z.string(), // e.g., "Grade 4"
      year: z.string(), // e.g., "2024-2025"
      tagline: z.string().optional(),
    }),
  }),
};
