# Astro Content Collections Reference

Source: https://docs.astro.build/en/guides/content-collections/

## Key Concepts

### Defining Collections

```ts
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const blog = defineCollection({
  loader: glob({ base: './src/content/blog', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
  }),
});

export const collections = { blog };
```

### Querying Collections

```astro
---
import { getCollection, getEntry } from 'astro:content';

// Get all entries
const allPosts = await getCollection('blog');

// Get single entry
const post = await getEntry('blog', 'post-id');
---
```

### Rendering Content (Key Section!)

To render markdown content, use the `render()` function from `astro:content`:

```astro
---
import { getEntry, render } from "astro:content";

const entry = await getEntry("blog", "post-1");
if (!entry) {
  throw new Error("Entry not found");
}
const { Content } = await render(entry);
---
<h1>{entry.data.title}</h1>
<Content />
```

### Generating Static Routes

```astro
---
import { getCollection, render } from 'astro:content';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  return posts.map(post => ({
    params: { id: post.id },
    props: { post },
  }));
}

const { post } = Astro.props;
const { Content } = await render(post);
---
<h1>{post.data.title}</h1>
<Content />
```

## Entry Properties

Each entry from `getCollection()` or `getEntry()` has:
- `id` - Unique identifier
- `data` - Frontmatter/data object matching schema
- `body` - Raw markdown body (for md/mdx files)
- `collection` - Collection name
- `rendered` - Pre-rendered HTML with `html` and `metadata` properties
