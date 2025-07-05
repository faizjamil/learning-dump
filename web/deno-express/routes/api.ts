import express from 'express';

const router = express.Router();

/* GET users listing. */
router.get('/', (_req: any, res: any) => {
  res.json({
    success: true,
    message: 'API Up!'
  });
});

export default router;
