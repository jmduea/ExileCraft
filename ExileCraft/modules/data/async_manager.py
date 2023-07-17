#   MIT License
#
#   Copyright (c) 2023 Jon Duea
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.

import asyncio
import os

import aiosqlite

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from modules.data.models.base_model import Base

BASE_DIR=os.path.dirname(os.path.realpath(__file__))


class TransactionManager():
    def __init__(self):
        self.engine = create_async_engine(
            "sqlite+aiosqlite:///exilecraft2.db",
            echo=True
        )
        self.session = async_sessionmaker(bind=self.engine, expire_on_commit=False)
        async with self.session as session:
            await session.run_sync(Base.metadata.create_all)
            
    async def get_session(self):
        async with self.session() as session:
            return session
      
      
if __name__ == "__main__":
    transaction_manager = TransactionManager()
    session = asyncio.run(transaction_manager.get_session())
    print(session)
    
