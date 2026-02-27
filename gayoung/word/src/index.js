import { Command } from 'commander';
import { add, list, remove, edit } from './cmd.js';

const program = new Command();

program
 .command('add')
 .argument('<word>')
 .description('메모 추가')
 .action( add );

 program
 .command('list')
 .description('목록 보기')
 .action( list );

 program
 .command('remove')
 .argument('<word>')
 .description('메모 삭제')
 .action( remove );

  program
 .command('edit')
 .argument('<word>')
 .argument('<editword>')
 .description('메모 수정')
 .action( edit );
   
   
 program.parse(process.argv);